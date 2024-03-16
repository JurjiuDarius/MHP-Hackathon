import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BookDeskDialogComponent } from './book-desk-dialog.component';

describe('BookDeskDialogComponent', () => {
  let component: BookDeskDialogComponent;
  let fixture: ComponentFixture<BookDeskDialogComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [BookDeskDialogComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(BookDeskDialogComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
