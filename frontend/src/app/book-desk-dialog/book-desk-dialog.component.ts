import { Component, Inject } from '@angular/core';
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
import { NgForOf, NgIf } from '@angular/common';
import { MatButton } from '@angular/material/button';
import { User } from '../models/user';
import { UserService } from '../service/user.service';
import { BookingService } from '../service/booking.service';

@Component({
  selector: 'app-book-desk-dialog',
  standalone: true,
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
  ],
  templateUrl: './book-desk-dialog.component.html',
  styleUrl: './book-desk-dialog.component.scss',
})
export class BookDeskDialogComponent {
  people: string[] = ['Item 1', 'Item 2', 'Item 3'];
  public users: User[] = [];
  public bookings: Booking[] = [];
  selectedPeople: string[] = [];

  constructor(
    public dialogRef: MatDialogRef<BookDeskDialogComponent>,
    @Inject(MAT_DIALOG_DATA) public data: Booking,
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

  onConfirm(): void {
    this.bookingService.createBooking(this.data);
    this.dialogRef.close();
  }
}
