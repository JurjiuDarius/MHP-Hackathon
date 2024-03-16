import { Component } from '@angular/core';
import {DatePipe, NgForOf, NgIf} from "@angular/common";
import {MatCard, MatCardContent} from "@angular/material/card";
import {Booking} from "../models/booking";
import {BookingService} from "../service/booking.service";

@Component({
  selector: 'app-ongoing-bookings',
  templateUrl: './ongoing-bookings.component.html',
  styleUrl: './ongoing-bookings.component.scss'
})
export class OngoingBookingsComponent {

  public bookings: Booking[] = [];

  constructor(private bookingService: BookingService) {
    this.bookingService.getBookings().subscribe({
      next: (response) => {
        this.bookings = response;
      },
      error: (error) => {
        console.log(error);
      },
    });
  }

  deleteBooking(bookingID: number) {
    this.bookingService.deleteBooking(bookingID).subscribe({
      next: (response) => {
        this.bookings = this.bookings.filter(
          (booking) => booking.id !== bookingID
        );
      },
      error: (error) => {
        console.log(error);
      },
    });
  }
  goToDetails(bookingID: number) {}
}
