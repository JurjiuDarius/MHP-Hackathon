import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MixedchartComponent } from './mixedchart.component';

describe('MixedchartComponent', () => {
  let component: MixedchartComponent;
  let fixture: ComponentFixture<MixedchartComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [MixedchartComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(MixedchartComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
