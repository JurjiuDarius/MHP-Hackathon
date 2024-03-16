import { TestBed } from '@angular/core/testing';

import { BookableService } from './bookable.service';

describe('BookableService', () => {
  let service: BookableService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(BookableService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
