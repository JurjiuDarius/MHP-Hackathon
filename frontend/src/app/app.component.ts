import { Component } from '@angular/core';
import { AuthenticationService } from './auth/service/authentication.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent {
  title = 'frontend';
  currentRole: string | null = 'user';
  public navDictionary: any = {
    employee: [
      { label: 'New Booking', path: '/new-booking' },
      { label: 'My Bookings', path: '/my-bookings' },
    ],
    admin: [
      { label: 'Statistics', path: '/' },
      { label: 'New Booking', path: '/patients' },
      { label: 'My Bookings', path: '/profile' },
    ],
  };
  public navItems: any;

  constructor(
    private authService: AuthenticationService,
    private router: Router
  ) {
    this.setRole();
    this.authService.getAuthChanges().subscribe((isAuthenticated) => {
      this.setRole();
    });
  }
  public logOut(): void {
    this.authService.logOut();
    this.router.navigate(['/login']);
  }

  private setRole() {
    const role = localStorage.getItem('currentRole');
    if (role) {
      this.currentRole = role;
    } else {
      this.currentRole = null;
    }
    if (this.currentRole != null) {
      this.navItems = this.navDictionary[this.currentRole];
    }
  }
}
