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
  private userId: number = 0;

  constructor(private bookingService: BookingService) {
    this.userId = parseInt(localStorage.getItem('currentUserId')!);
    this.bookingService.getPastBookingsForUser(this.userId).subscribe({
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
