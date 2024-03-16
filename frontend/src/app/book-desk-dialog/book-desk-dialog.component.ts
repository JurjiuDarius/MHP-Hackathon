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
    private bookingService: BookingService
  ) {
    this.userService.getUsers().subscribe({
      next: (response) => {
        this.users = response;
      },
      error: (error) => {
        console.log(error);
      },
    });

    this.bookingService.getBookings().subscribe({
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

  getFormattedDate(currentDate: Date): string {
    if (currentDate) {
      return this.datePipe.transform(currentDate, 'dd/MM/yyyy') || '';
    }
    return '';
  }

  onConfirm(): void {
    console.log(this.selectedPeople);
    console.log(this.data);
    if (this.data.date.length == 0) {
      const currentDate = new Date();
      this.data.date = this.getFormattedDate(currentDate);
    }
    this.data.start = this.startTime;
    this.data.end = this.endTime;
    this.bookingService.createBooking(this.data).subscribe();
    this.dialogRef.close();
  }
}
