import { Component } from '@angular/core';
import { Booking } from '../models/booking';
import { BookingService } from '../service/booking.service';
@Component({
  selector: 'app-my-bookings',
  templateUrl: './my-bookings.component.html',
  styleUrl: './my-bookings.component.scss',
})
export class MyBookingsComponent {
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
  goToDetails(booking: Booking) {}
}
