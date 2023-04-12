import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddClubFormComponent } from './add-club-form.component';

describe('AddClubFormComponent', () => {
  let component: AddClubFormComponent;
  let fixture: ComponentFixture<AddClubFormComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AddClubFormComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AddClubFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
