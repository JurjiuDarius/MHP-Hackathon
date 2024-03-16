import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './auth/login/login.component';
import { MyBookingsComponent } from './my-bookings/my-bookings.component';
import { FloorMapComponent } from './floor-map/floor-map.component';
import { PiechartComponent } from './piechart/piechart.component';
import { NgApexchartsModule } from 'ng-apexcharts';

import { UserPageComponent } from './user-page/user-page.component';
const routes: Routes = [
  { path: '', redirectTo: 'login', pathMatch: 'full' },
  {
    path: 'login',
    component: LoginComponent,
  },
  // { path: 'my-bookings', component: MyBookingsComponent },
  { path: 'new-booking', component: FloorMapComponent },
  { path: 'piechart', component: PiechartComponent },
  { path: 'user-profile', component: UserPageComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
