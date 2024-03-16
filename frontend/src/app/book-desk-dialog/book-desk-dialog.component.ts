import {Component, Inject} from '@angular/core';
import {MAT_DIALOG_DATA, MatDialogActions, MatDialogContent, MatDialogRef} from "@angular/material/dialog";
import {Booking} from "../models/booking";
import {MatCard, MatCardContent, MatCardHeader} from "@angular/material/card";
import {MatFormField, MatLabel} from "@angular/material/form-field";
import {MatOption, MatSelect} from "@angular/material/select";
import {MatCheckbox} from "@angular/material/checkbox";
import {NgForOf} from "@angular/common";
import {MatButton} from "@angular/material/button";

@Component({
  selector: 'app-book-desk-dialog',
  standalone: true,
  imports: [
    MatDialogActions,
    MatDialogContent,
    MatCard,
    MatCardContent,
    MatFormField,
    MatSelect,
    MatOption,
    MatLabel,
    MatCheckbox,
    NgForOf,
    MatCardHeader,
    MatButton
  ],
  templateUrl: './book-desk-dialog.component.html',
  styleUrl: './book-desk-dialog.component.scss'
})
export class BookDeskDialogComponent {

  people: string[] = ['Item 1', 'Item 2', 'Item 3'];
  selectedPeople: string[] = [];

  constructor(public dialogRef: MatDialogRef<BookDeskDialogComponent>,
              @Inject(MAT_DIALOG_DATA) public data: string){ }

  toggleSelection(person: string) {
    if (this.selectedPeople.includes(person)) {
      this.selectedPeople = this.selectedPeople.filter(p => p !== person);
    } else {
      this.selectedPeople.push(person);
    }
    // console.log('Selected people:', this.selectedPeople);
    // You can perform any additional logic here
  }

  onCancel(): void {
    this.dialogRef.close();
  }

  onConfirm(): void {
    // Perform confirmation logic here
    console.log(this.selectedPeople)
    console.log(this.data)
    this.dialogRef.close();
  }

}
