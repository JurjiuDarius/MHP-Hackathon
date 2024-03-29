import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './auth/login/login.component';
import { MatCard, MatCardModule } from '@angular/material/card';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MatFormFieldModule, MatLabel } from '@angular/material/form-field';
import { MatRadioModule } from '@angular/material/radio';
import { HTTP_INTERCEPTORS, HttpClientModule } from '@angular/common/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatInputModule } from '@angular/material/input';
import { provideAnimationsAsync } from '@angular/platform-browser/animations/async';
import { MyBookingsComponent } from './my-bookings/my-bookings.component';
import { FloorMapComponent } from './floor-map/floor-map.component';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatTooltipModule } from '@angular/material/tooltip';

import { PiechartComponent } from './piechart/piechart.component';
import { Component, ViewChild } from '@angular/core';
import {
  MatCalendar,
  MatDatepicker,
  MatDatepickerInput,
  MatDatepickerToggle,
} from '@angular/material/datepicker';

import { NgApexchartsModule } from 'ng-apexcharts';
import { MatMomentDateModule } from '@angular/material-moment-adapter';
import { UserPageComponent } from './user-page/user-page.component';
import { MatTab, MatTabGroup, MatTabLabel } from '@angular/material/tabs';
import { OngoingBookingsComponent } from './ongoing-bookings/ongoing-bookings.component';
import { MatSelectModule } from '@angular/material/select';
import { BookDeskDialogComponent } from './book-desk-dialog/book-desk-dialog.component';
import { MatSnackBarModule } from '@angular/material/snack-bar';
import {
  MatCell,
  MatHeaderCell,
  MatHeaderRow,
  MatRow,
  MatTable,
  MatTableModule,
} from '@angular/material/table';
import { AdminPageComponent } from './admin-page/admin-page.component';
import * as ApexCharts from 'apexcharts';
import { TokenInterceptor } from './service/http-interceptor';
@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    MyBookingsComponent,
    FloorMapComponent,
    UserPageComponent,
    OngoingBookingsComponent,
    AdminPageComponent,
    PiechartComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    ReactiveFormsModule,
    MatFormFieldModule,
    MatInputModule,
    MatRadioModule,
    HttpClientModule,
    MatCardModule,
    MatToolbarModule,
    MatButtonModule,
    MatIconModule,
    MatTooltipModule,
    MatDatepickerToggle,
    MatDatepicker,
    MatDatepickerInput,
    MatMomentDateModule,
    MatTabGroup,
    MatTab,
    MatTabLabel,
    MatFormFieldModule,
    MatInputModule,
    MatSelectModule,
    FormsModule,
    MatSnackBarModule,
    MatHeaderCell,
    MatCell,
    MatHeaderRow,
    MatRow,
    MatTableModule,
    MatCalendar,
  ],
  providers: [
    provideAnimationsAsync(),
    {
      provide: HTTP_INTERCEPTORS,
      useClass: TokenInterceptor,
      multi: true,
    },
  ],
  bootstrap: [AppComponent],
  exports: [MyBookingsComponent],
})
export class AppModule {}
