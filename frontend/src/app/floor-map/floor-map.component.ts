import {Component, ViewEncapsulation} from '@angular/core';
import {MatCalendarCellClassFunction} from "@angular/material/datepicker";
import {provideNativeDateAdapter} from "@angular/material/core";

@Component({
  selector: 'app-floor-map',
  templateUrl: './floor-map.component.html',
  providers: [provideNativeDateAdapter()],
  styleUrls: ['./floor-map.component.scss']
})
export class FloorMapComponent {

  dateClass: MatCalendarCellClassFunction<Date> = (cellDate, view) => {
    if (view === 'month') {
      const date = cellDate.getDate();

      if (date === 1 || date === 20)
        return 'fully-booked-date';

      if (date % 5 ===0)
        return 'partially-booked-date';
    }
    return '';
  };
}
