import {Component, Inject} from '@angular/core';
import {MAT_DIALOG_DATA, MatDialogRef} from "@angular/material/dialog";
import {Booking} from "../models/booking";
import {DatePipe} from "@angular/common";
import {UserService} from "../service/user.service";
import {BookingService} from "../service/booking.service";
import {User} from "../models/user";

@Component({
  selector: 'app-user-page',
  templateUrl: './user-page.component.html',
  styleUrls: ['./user-page.component.scss']
})
export class UserPageComponent {
  currentUserId = JSON.parse(localStorage.getItem('user') || '{}');
  users:User[]=[];
  currentUser:string | undefined='';
  constructor(
    private userService: UserService,
  ) {
    this.userService.getUsers().subscribe({
      next: (response) => {
        this.users = response;
      },
      error: (error) => {
        console.log(error);
      },
    });

    this.currentUser=this.users.find(item => item.id === this.currentUserId)?.username

  }


}
