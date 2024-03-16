import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './auth/login/login.component';
import { MyBookingsComponent } from './my-bookings/my-bookings.component';
import { FloorMapComponent } from './floor-map/floor-map.component';
import { PiechartComponent } from './piechart/piechart.component';
import { MixedchartComponent } from './mixedchart/mixedchart.component';
import { NgApexchartsModule } from "ng-apexcharts";

const routes: Routes = [
  { path: '', redirectTo: 'login', pathMatch: 'full' },
  {
    path: 'login',
    component: LoginComponent,
  },
  { path: 'my-bookings', component: MyBookingsComponent },
  { path: 'new-booking', component: FloorMapComponent },
  { path: 'piechart', component: PiechartComponent },
  { path: 'mixedchart', component: MixedchartComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
