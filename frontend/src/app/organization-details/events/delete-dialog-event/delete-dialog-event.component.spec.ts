import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DeleteDialogEventComponent } from './delete-dialog-event.component';

describe('DeleteDialogEventComponent', () => {
  let component: DeleteDialogEventComponent;
  let fixture: ComponentFixture<DeleteDialogEventComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DeleteDialogEventComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DeleteDialogEventComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
