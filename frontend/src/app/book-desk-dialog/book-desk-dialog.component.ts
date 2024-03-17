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
import { BookingService } from '../service/booking.service';
import { FormsModule } from '@angular/forms';
import { MatSnackBar } from '@angular/material/snack-bar';
import { Bookable } from '../models/bookable';
import { UserService } from '../service/user.service';
import { BookableService } from '../service/bookable.service';
import {
  MatCell,
  MatColumnDef,
  MatHeaderCell,
  MatRow,
  MatTable,
} from '@angular/material/table';
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
    MatTable,
    MatColumnDef,
    MatHeaderCell,
    MatCell,
    MatRow,
  ],
  templateUrl: './book-desk-dialog.component.html',
  styleUrl: './book-desk-dialog.component.scss',
})
export class BookDeskDialogComponent {
  public users: User[] = [];
  public bookings: Booking[] = [];
  public capacity: number = 0;
  public availabilityMorning: number | null = null;
  public availabilityEvening: number | null = null;
  selectedPeople: string[] = [];
  startTime: string = '';
  endTime: string = '';
  bookableList: Bookable[] = [];

  constructor(
    public dialogRef: MatDialogRef<BookDeskDialogComponent>,
    @Inject(MAT_DIALOG_DATA) public data: any,
    private datePipe: DatePipe,
    private userService: UserService,
    private bookingService: BookingService,
    private bookableService: BookableService,
    private snackbar: MatSnackBar
  ) {
    // Add some sample bookings to the bookings array

    if (this.data.bookable_id.startsWith('CLUJ')) {
      this.bookableService
        .getAvailabilityForBookable(data.bookable_id, data.date)
        .subscribe({
          next: (response) => {
            this.availabilityMorning = response[0] * 100;
            this.availabilityEvening = response[1] * 100;
          },
          error: (error) => {
            console.log(error);
          },
        });
    }
    this.bookableService.getCapacityForBookable(data.bookable_id).subscribe({
      next: (response) => {
        this.capacity = response;
      },
      error: (error) => {
        console.log(error);
      },
    });

    this.userService.getUsers().subscribe({
      next: (response) => {
        this.users = response;
      },
      error: (error) => {
        console.log(error);
      },
    });
    this.bookingService
      .getBookingsByDate(data.date, data.bookable_id)
      .subscribe({
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
    // check if start time is before end time

    //check if at least half the capacity is occupied
    if (
      this.capacity != 1 &&
      this.selectedPeople.length + 1 < this.capacity / 2
    ) {
      this.snackbar.open(
        'At least half the capacity of the room needs to be occupied !',
        'Close',
        {
          duration: 2000,
        }
      );
      return;
    }
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
    this.data.people = this.selectedPeople;

    this.bookingService.createBooking(this.data).subscribe();
    this.dialogRef.close();
  }
}
