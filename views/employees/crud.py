from dataclasses import dataclass, field
from .schemas import Employee, EmployeeCreate
from typing import List, Optional


@dataclass
class EmployeeStorage:
    last_id: int = 0
    employees: dict[int, Employee] = field(default_factory=dict)

    @property
    def next_id(self) -> int:
        self.last_id += 1
        return self.last_id

    def create_employee(self, employee_create: EmployeeCreate) -> Employee:
        employee = Employee(
            id = self.next_id,
            **employee_create.model_dump(),
        )
        self.employees[employee.id] = employee
        return employee

    def get_employees(self) -> List[Employee]:
        return list(self.employees.values())

    def get_employee_by_id(self, id: int) -> Optional[Employee]:
        return self.employees.get(id)

    def remove_employee_by_id(self, id: int) -> None:
        if id in self.employees:
            del self.employees[id]


storage = EmployeeStorage()