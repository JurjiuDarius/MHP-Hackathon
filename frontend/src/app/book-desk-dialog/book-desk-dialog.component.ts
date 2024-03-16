import {
  AfterViewInit,
  Component,
  ElementRef,
  Inject,
  ViewChild,
} from '@angular/core';
import {
  MAT_DIALOG_DATA,
  MatDialogActions,
  MatDialogContent,
  MatDialogRef,
} from '@angular/material/dialog';
import { Booking } from '../models/booking';
import { MatCard, MatCardContent, MatCardHeader } from '@angular/material/card';
import { MatFormField, MatLabel } from '@angular/material/form-field';
import { MatOption, MatSelect } from '@angular/material/select';
import { MatCheckbox } from '@angular/material/checkbox';
import { DatePipe, NgForOf, NgIf } from '@angular/common';
import { MatButton } from '@angular/material/button';
import { User } from '../models/user';
import { UserService } from '../service/user.service';
import { BookingService } from '../service/booking.service';
import { FormsModule } from '@angular/forms';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
  selector: 'app-book-desk-dialog',
  standalone: true,
  providers: [DatePipe],
  imports: [
    MatDialogActions,
    MatDialogContent,
    MatCard,
    MatCardContent,
    MatFormField,
    MatSelect,
    MatOption,
    MatLabel,
    MatCheckbox,
    NgForOf,
    MatCardHeader,
    MatButton,
    NgIf,
    FormsModule,
  ],
  templateUrl: './book-desk-dialog.component.html',
  styleUrl: './book-desk-dialog.component.scss',
})
export class BookDeskDialogComponent {
  public users: User[] = [];
  public bookings: Booking[] = [];
  selectedPeople: string[] = [];
  startTime: string = '';
  endTime: string = '';

  constructor(
    public dialogRef: MatDialogRef<BookDeskDialogComponent>,
    @Inject(MAT_DIALOG_DATA) public data: Booking,
    private datePipe: DatePipe,
    private userService: UserService,
    private bookingService: BookingService,
    private snackbar: MatSnackBar
  ) {
    this.userService.getUsers().subscribe({
      next: (response) => {
        this.users = response;
      },
      error: (error) => {
        console.log(error);
      },
    });
    this.bookingService.getBookingsByDate(data.date).subscribe({
      next: (response) => {
        this.bookings = response;
      },
      error: (error) => {
        console.log(error);
      },
    });
  }

  toggleSelection(person: string) {
    if (this.selectedPeople.includes(person)) {
      this.selectedPeople = this.selectedPeople.filter((p) => p !== person);
    } else {
      this.selectedPeople.push(person);
    }
  }

  onCancel(): void {
    this.dialogRef.close();
  }

  onConfirm(): void {
    console.log(this.selectedPeople);
    console.log(this.data);
    // check if start time is before end time
    if (this.startTime >= this.endTime) {
      this.snackbar.open(
        'The start time needs to be before the end time !',
        'Close',
        {
          duration: 2000,
        }
      );
      return;
    }
    //check if there are other bookings for the same desk
    for (let booking of this.bookings) {
      if (booking.bookable_id === this.data.bookable_id) {
        if (
          (this.startTime >= booking.start && this.startTime <= booking.end) ||
          (this.endTime >= booking.start && this.endTime <= booking.end) ||
          (this.startTime <= booking.start && this.endTime >= booking.end)
        ) {
          this.snackbar.open(
            'The desk is already booked for the selected time interval !',
            'Close',
            {
              duration: 2000,
            }
          );
          return;
        }
      }
    }

    this.data.start = this.startTime;
    this.data.end = this.endTime;
    this.bookingService.createBooking(this.data).subscribe();
    this.dialogRef.close();
  }
}
