import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthenticationService } from '../service/authentication.service';
import { concat } from 'rxjs';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
})
export class LoginComponent {
  loginForm: FormGroup;
  errorCode: String | null = null;
  errorMessage: String | null = null;
  constructor(
    private formBuilder: FormBuilder,
    private authService: AuthenticationService,
    private router: Router
  ) {
    console.log('LoginComponent constructor');
    this.authService.logOut();
    this.loginForm = this.formBuilder.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(8)]],
      role: ['', Validators.required],
    });
  }

  onSubmit() {
    if (this.loginForm.valid) {
      this.authService
        .logIn(
          this.loginForm.get('email')?.value,
          this.loginForm.get('password')?.value,
          this.loginForm.get('role')?.value
        )
        .subscribe({
          next: (response) => {
            this.router.navigate(['/appointments']);
          },
          error: (error) => {
            this.errorCode = error.status;
            this.errorMessage = error.error.message;
          },
        });
    }
  }
  goToSignup() {
    this.router.navigate(['/signup']);
  }
}
