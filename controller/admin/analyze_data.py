from flask import render_template, Blueprint
from mindspore import context, Tensor, dtype as mstype
import mindspore.nn as nn

admin_analyze_data_controller = Blueprint('admin_analyze_data', __name__)

# Set up MindSpore context
context.set_context(mode=context.GRAPH_MODE)

# Define a simple mathematical operation
class SimpleMathOperation(nn.Cell):
    def construct(self, x, y):
        # Addition operation
        result = x + y
        return result

# Flask route
@admin_analyze_data_controller.route('/admin/analyze_data')
def admin_route():
    # Instantiate the simple math operation model
    math_model = SimpleMathOperation()

    # Create some input values
    x_input = Tensor(8.0, dtype=mstype.float32)
    y_input = Tensor(5.0, dtype=mstype.float32)

    # Perform the mathematical operation
    result = math_model(x_input, y_input)

    # Pass the result to the template
    return render_template('/admin/analyze_data.html', result=result.asnumpy())
