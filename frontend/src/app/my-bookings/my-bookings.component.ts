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

  getCurrentDate(): Date {
    return new Date();
  }

  isPastDate(date: String): boolean {
    return date < this.getCurrentDate().toString();
  }

  goToDetails(bookingID: number) {}
}
