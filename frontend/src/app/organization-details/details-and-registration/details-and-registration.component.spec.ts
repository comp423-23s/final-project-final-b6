import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DetailsAndRegistrationComponent } from './details-and-registration.component';

describe('DetailsAndRegistrationComponent', () => {
  let component: DetailsAndRegistrationComponent;
  let fixture: ComponentFixture<DetailsAndRegistrationComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DetailsAndRegistrationComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DetailsAndRegistrationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
